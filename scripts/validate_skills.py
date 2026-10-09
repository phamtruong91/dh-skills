"""Validate package contracts; not a legal compliance certification."""
from pathlib import Path
import json,re
import yaml

ROOT=Path(__file__).resolve().parents[1]
def validate():
    manifest=json.loads((ROOT/'skills-manifest.json').read_text())
    skills=sorted((ROOT/'skills').glob('*/SKILL.md')); errors=[]
    assert len(skills)==manifest['count']==171
    records={x['name']:x for x in manifest['skills']}
    for p in skills:
        name=p.parent.name;t=p.read_text()
        fm=yaml.safe_load(t.split('---',2)[1]);ui=yaml.safe_load((p.parent/'agents/openai.yaml').read_text())['interface']
        checks=[fm['name']==name,bool(re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',name)),len(name)<=64,len(fm['description'])<=1024,25<=len(ui['short_description'])<=64,'$'+name in ui['default_prompt'],bool(ui['display_name']),'## Quản trị phiên bản' in t,'## Giới hạn và human gate' in t,'(đã ký)' not in t]
        version=json.loads((p.parent/'references/version.json').read_text());checks+=[version==records[name],version['version']=='1.2.1',version['approval_owner'] is None]
        if version['legal_updates']:checks.extend([(p.parent/'references/phap-ly.md').exists(),(p.parent/'references/quy-trinh-lich-su.md').exists(),'[CẦN XÁC MINH]' in t])
        for link in re.findall(r'\]\((references/[^)]+)\)',t):checks.append((p.parent/link).is_file())
        output=p.parent/version['output_reference'];checks.extend([output.is_file(),version['missing_data_policy']=='preserve-template-fill-spaces',version['qa_attachments'] is False])
        output_text=output.read_text()
        checks.extend(['## Cấu trúc sản phẩm của skill' in output_text, '## Quy tắc giao văn bản' in output_text, 'chừa chỗ điền đúng mẫu gốc' in output_text, 'Không dùng dấu ba chấm' not in output_text, '[CHỜ KÝ]' not in t, 'Mọi đầu ra mặc định là **DỰ THẢO' not in t, '## Đầu ra' in t])
        for link in re.findall(r'\]\(([^)]+)\)',output_text):
            if not link.startswith(('https://','http://')):checks.append((output.parent/link).is_file())
        if not all(checks):errors.append(name)
    assert not errors,errors
    # Regression contracts for meaningful defects and legal applicability gates.
    cv=(ROOT/'skills/soan-cong-van/SKILL.md').read_text();assert 'TUQ. HIỆU TRƯỞNG' in cv
    assert 'không dùng chữ CV' in cv and 'lấy số tiếp theo' not in cv
    meeting=(ROOT/'skills/soan-bien-ban-hop/references/quy-cach-dau-ra.md').read_text();assert 'Mẫu 1.9' in meeting and 'số, ký hiệu' in meeting
    financial=(ROOT/'skills/bao-cao-tai-chinh/references/quy-cach-dau-ra.md').read_text();assert all(x in financial for x in ['B01/BCTC','B02/BCTC','B03/BCTC','B04/BCTC'])
    council=(ROOT/'skills/chuan-bi-hop-hoi-dong-truong/SKILL.md').read_text();assert 'Không dùng để tổ chức hoạt động mới' in council
    assert '`thanh_vien`' not in (ROOT/'skills/chuan-bi-hop-hoi-dong-truong/references/quy-trinh-lich-su.md').read_text()
    buying=(ROOT/'skills/ke-hoach-mua-sam/SKILL.md').read_text();assert 'Không suy ra chỉ định thầu/mua sắm trực tiếp chỉ vì nhỏ lẻ hoặc cấp bách' in buying
    graduate=(ROOT/'skills/quyet-dinh-tot-nghiep/SKILL.md').read_text();assert 'Không tự triệu tập hội đồng lần nữa' in graduate
    print(json.dumps({'skills':len(skills),'interface_metadata':len(skills),'version_records':len(records),'targeted_legal_updates':sum(bool(x['legal_updates']) for x in records.values()),'errors':errors},ensure_ascii=False))

if __name__=='__main__':validate()
