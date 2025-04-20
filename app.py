
from docxtpl import DocxTemplate
from flask import Flask, request, send_file
import tempfile
from datetime import datetime

app = Flask(__name__)

def format_date(date_str):
    try:
        return datetime.strptime(date_str, "%d.%m.%Y").strftime("%-d. %-m. %Y")
    except Exception:
        return date_str

@app.route("/api/generate", methods=["POST"])
def generate_doc():
    data = request.get_json()

    values = {
        "cislo_smlouvy": data.get("cislo_smlouvy", ""),
        "cislo_partnera": data.get("cislo_partnera", ""),
        "jmeno": data.get("jmeno", ""),
        "prijmeni": data.get("prijmeni", ""),
        "datum_narozeni": format_date(data.get("datum_narozeni", "")),
        "ulice_trvala": data.get("ulice_trvala", ""),
        "mesto_trvala": data.get("mesto_trvala", ""),
        "psc_trvala": data.get("psc_trvala", ""),
        "email": data.get("email", ""),
        "telefon": data.get("telefon", ""),
        "zpusob_odesilani": data.get("zpusob_odesilani", ""),
        "platby_faktury": data.get("platby_faktury", ""),
        "platby_zalohy": data.get("platby_zalohy", ""),
        "cislo_uctu": data.get("cislo_uctu", ""),
        "zahajeni_dodavek": format_date(data.get("zahajeni_dodavek", "")),
        "prolongace": format_date(data.get("prolongace", "")),
        "ean": data.get("ean", ""),
        "ulice_odber": data.get("ulice_odber", ""),
        "mesto_odber": data.get("mesto_odber", ""),
        "psc_odber": data.get("psc_odber", "")
    }

    doc = DocxTemplate("Rekapitulace_Domacnost_Plyn.docx")
    doc.render(values)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        doc.save(tmp.name)
        return send_file(tmp.name, as_attachment=True, download_name="smlouva_plyn.docx")
