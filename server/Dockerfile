FROM python:3.10
# 
WORKDIR /code
# 
COPY . /code
# 
RUN pip3 install -r /code/requirements.txt
# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]