# coding:utf-8
import os
import shutil
import glob
import urllib.parse
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

MAINTENANCE_PATH="/leete_latobarita_uruth_ariaroth_bal_netoreel"
BALSE_PATH="/balse"

FLASK_TEMPLATES_FOLDER="templates"
MAINTENANCE_PAGE="laputa.html"

# Open the maintenance page.
@app.route(MAINTENANCE_PATH)
def leete_latobarita_uruth_ariaroth_bal_netoreel():
    if os.path.isfile(os.path.join(FLASK_TEMPLATES_FOLDER,MAINTENANCE_PAGE))==False:
        return "This website has been balsed by someone."
    return render_template(MAINTENANCE_PAGE)

# Delete all files and folders except this_file.
@app.route(BALSE_PATH, methods=['GET'])
def balse():
    if urllib.parse.urljoin(request.url_root,MAINTENANCE_PATH) != request.referrer:
        return "Refused."

    files=os.listdir("./")
    this_file=os.path.basename(__file__)

    print("-∴-∵-∴-∵-∴-∵-∴-∵-∴-∵ BALSE!! ∴-∵-∴-∵-∴-∵-∴-∵-∴-∵-∴-")

    for file in files:
        if file==this_file:
            continue
        print(file)
        if os.path.isdir(file)==True:
            shutil.rmtree(file)
        else:
            os.remove(file)

    return "Balsed."


# Start the server.
if __name__ == "__main__":
    app.run()
