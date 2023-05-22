import sqlite3
import logging

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from starlette import status

logging.basicConfig(
    format="{asctime} {levelname:<8} {message}",
    style="{"
)


class Company(BaseModel):
    cnpj_cia: str
    denom_social: str
    denom_comerc: str
    dt_reg: str
    dt_const: str
    dt_cancel: str
    motivo_cancel: str
    sit: str
    dt_ini_sit: str
    cd_cvm: str
    setor_ativ: str
    tp_merc: str
    categ_reg: str
    dt_ini_categ: str
    sit_emissor: str
    dt_ini_sit_emissor: str
    controle_acionario: str
    tp_ender: str
    logradouro: str
    comple: str
    bairro: str
    mun: str
    uf: str
    pais: str
    cep: str
    ddd_tel: str
    tel: str
    ddd_fax: str
    fax: str
    email: str
    tp_resp: str
    resp: str
    dt_ini_resp: str
    logradouro_resp: str
    comple_resp: str
    bairro_resp: str
    mun_resp: str
    uf_resp: str
    pais_resp: str
    cep_resp: str
    ddd_tel_resp: str
    tel_resp: str
    ddd_fax_resp: str
    fax_resp: str
    email_resp: str
    cnpj_auditor: str
    auditor: str


app = FastAPI()


@app.get("/")
def get_root():
    return {"InfoInvest": "AI"}


@app.get("/companies")
def get_companies():
    # Create a connection to the database
    conn = sqlite3.connect("C:\\Users\\Max\\PycharmProjects\\infoinvest_ai\\companies.sqlite")

    # Create a cursor object
    cur = conn.cursor()

    # Get the company by CNPJ
    cur.execute("SELECT * FROM companies LIMIT 10")
    company = cur.fetchmany(10)

    # Close the connection to the database
    conn.close()

    return jsonable_encoder(company)


@app.get("/companies/{cnpj}")
def get_company_by_cnpj(cnpj: str):
    # Create a connection to the database
    if len(cnpj) != 14:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    conn = sqlite3.connect("C:\\Users\\Max\\PycharmProjects\\infoinvest_ai\\companies.sqlite")
    cnpj_format = cnpj[:2] + "." + cnpj[2:5] + "." + cnpj[5:8] + "/" + cnpj[8:12] + "-" + cnpj[12:14]

    # Create a cursor object
    cur = conn.cursor()

    # Get the company by CNPJ
    sql = f"SELECT * FROM companies WHERE CNPJ_CIA = '{cnpj_format}'"
    logging.warning("This is the sql command = " + sql)
    cur.execute(sql)
    company = cur.fetchone()

    if company is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Item not found"
                            )

    # Close the connection to the database
    conn.close()

    return jsonable_encoder(company)

if __name__ == "__main__":
    app.run(debug=True)
