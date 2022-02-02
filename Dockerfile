FROM python:3.8
ADD main.py .
RUN pip install tk 

CMD ["./main.py"]











