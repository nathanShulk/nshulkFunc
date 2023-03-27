import logging
import azure.functions as func
import requests
import xlsxwriter
from FlaskApp import app

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.HttpResponse(f"Hello moto")    


