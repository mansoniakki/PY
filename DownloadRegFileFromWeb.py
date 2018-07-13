from urllib import request

csv_url="https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv"

def download_reg_file(url):
    # reading the file from web
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    # defining destination
    dest_url = r"goog.csv"
    # opening destination file to write
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


download_reg_file(csv_url)






