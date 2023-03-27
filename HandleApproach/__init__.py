import logging
import azure.functions as func
import requests
import xlsxwriter
from FlaskApp import app


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    name = req.params.get('engineer')
    sr_num = req.params.get('sr')
    sev = req.params.get('sev')
    sap = req.params.get('sap')
    date_a = req.params.get('assigned')
    caseType = req.params.get('caseType')
    notes = req.params.get('notes')


    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    if not sr_num:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sr_num = req_body.get('sr_num')
    if not sev:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sev = req_body.get('sev')
    if not sap:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sap = req_body.get('sap')
    if not date_a:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            date_a = req_body.get('assigned')
    if not caseType:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            caseType = req_body.get('caseType')
    if not notes:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            notes = req_body.get('notes')

    if name:
        #msg.set(name)
        if sr_num:
            if sev:
                if sap:
                    if date_a:
                        if caseType:
                            return func.HttpResponse(f"Engineer Assigned: {name}\nSR #: {sr_num}\nSeverity: {sev}\nCase Type: {caseType}\nDate Assigned: {date_a}\nSAP: {sap}\n")    
                        return func.HttpResponse(f"Engineer Assigned: {name}\nSR #: {sr_num}\nSeverity: {sev}\nCase Type: Missing\nDate Assigned: {date_a}\nSAP: {sap}\n")    
                    return func.HttpResponse(f"Hello {name}, you called this function! but there is no date")
                return func.HttpResponse(f"Hello {name}, you called this function! but thre is no sap")
            return func.HttpResponse(f"Hello {name}, you called this function! but there is no sev")
        return func.HttpResponse(f"Hello {name}, you called this function! Woop")
    return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400
        )

