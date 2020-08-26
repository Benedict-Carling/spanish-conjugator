FROM python:3-onbuild

RUN pip install --upgrade pip

CMD ["python", "./src/spanishconjugator.py"]