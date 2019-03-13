import os


template_path   = os.path.join(os.path.dirname(__file__), "templates")
static_path     = os.path.join(os.path.dirname(__file__), "static")

#
database="test1"
user="postgres"
password="123"
host="localhost"
port=5432


home_page = {
    "title":"Главная страница"
}

pages = {
    "Asset":{
        "route"  : "Asset",
        "title" :"Месторождение",
        "head_table":['ID','Месторождение'],
        "request":"SELECT * FROM Asset"
    },
    "Well":{
        "route":"Well",
        "title":"Скважина",
        "head_table":['ID','Месторождение','Скважина','X','Y'],
        "request": "SELECT Well.id, Asset.name, Well.name, Well.X, Well.Y FROM Well,Asset WHERE Well.asset_id = Asset.id"
    },
    "Layer":{
        "route":"Layer",
        "title":"Пласт",
        "head_table":['ID','Месторождение','Пласт'],
        "request":"SELECT Layer.id, Asset.name, Layer.name FROM Layer, Asset WHERE Layer.asset_id = Asset.id"
    },
    "Intersection":{
        "route":"Intersection",
        "title":"Пластопересечение",
        "head_table":['ID','Скважина','Пласт','X','Y'],
        "request":"SELECT Intersection.id, Well.name, Layer.name,Intersection.X, Intersection.Y FROM Intersection, Well, Layer WHERE Intersection.well_id = Well.id AND Intersection.layer_id = Layer.id"
    }

}