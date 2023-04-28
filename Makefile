pythonf = main.py 2Auth.py
files =	geckodriver.log
RM = rm -f
green = '\033[92m'
py = python3

auth:	${py} ${pythonf}

clean:
	@${RM} ${files}
	@echo ${green} "file deleted"

.PHONY: auth clean