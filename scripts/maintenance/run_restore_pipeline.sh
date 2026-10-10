#!/bin/sh
# Chạy toàn bộ đợt khôi phục quy trình theo đúng thứ tự (chỉ chạy từ trạng thái trước khôi phục).
set -e
python3 -X utf8 scripts/maintenance/fix_phap_ly_text.py
python3 -X utf8 scripts/maintenance/restore_procedures.py | tail -1
python3 -X utf8 scripts/maintenance/label_diagrams.py --apply --rebuild | tail -1
python3 -X utf8 scripts/maintenance/polish_restored.py
