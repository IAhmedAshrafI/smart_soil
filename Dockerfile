FROM python:3.8.6

# Expose project's port
EXPOSE 9001

# Always set a working directory
WORKDIR /web

# Add the req. file and install the req
COPY requirments.txt requirments.txt
RUN pip --timeout=1000 install -r requirments.txt

# Copy all project to the image
COPY ./ ./

## Copy the entry point and change own for the .sh file
#COPY ./smart_soil.sh /
#RUN chmod +x smart_soil.sh
#
## Execute the entry point sh file
#ENTRYPOINT ["./smart_soil.sh"]

