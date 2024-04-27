source ../../../venv/bin/activate
pylint --output-format=json:somefile.json,colorized decrypt.py
pylint --output-format=json:somefile.json,colorized test/test_decrypt.py
pylint_res=$?
if [[ pylint_res -eq 0 ]]; then
  echo 'Pylint OK'
else
  echo 'Pylint not OK'
fi