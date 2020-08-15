export PIPENV_VENV_IN_PROJECT=.venv

demo: .venv
	source .venv/bin/activate; python3 demo.py
	# converted data/*.csv to .xlsx files
.PHONY: demo

venv:
	[[ -x "$(shell command -v python3)" ]]
	[[ -d .venv ]] || python3 -m venv .venv
.PHONY: venv

.venv: requirements.txt
	make venv
	source .venv/bin/activate; pip3 install -U pip -r requirements.txt
