# used a small python image
FROM python:3.6-alpine

# set workdir
WORKDIR /app

ADD requirements.txt /app/requirements.txt
# install packages from requirements.txt
RUN pip install -r requirements.txt

# copy folder
ADD . /app

# expose 80 port to outside
EXPOSE 80

# run command to execute python
ENTRYPOINT ["python"]
CMD ["microtalk.py"]
# CMD ["python", "microtalk.py"]