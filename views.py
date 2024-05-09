from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from datetime import date

homepage = Blueprint(__name__, "views")

@homepage.errorhandler(404) 
def not_found(e): 
  return render_template("404.html"), 404

@homepage.route("/")
def home():
    return render_template("index.html", today = date.today())

@homepage.route("/json")
def get_json():
    return jsonify({'name': 'PortableDenoiser', 'date': date.today()})

@homepage.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@homepage.route("/go-to-home")
def go_to_home():
    return redirect(url_for("homepage.home"))
