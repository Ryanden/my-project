#!/usr/bin/env bash
# .secrets와 staging area에 추가
git add -f .secrets

# eb deploy실행
eb deploy --profile fc-8th-eb --staged

# .secrets 를 제거
git reset HEAD .secrets


git reset
