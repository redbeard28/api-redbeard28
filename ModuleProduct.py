from flask import jsonify
import requests

def getproduct(code_barre):
#code_barre = 8002270014901

    url = "https://fr.openfoodfacts.org/api/v0/produit/{}.json".format(code_barre)
    r = requests.get(url)
    produit = r.json()
    # print(produit)
    produit_name = produit['product']['brands']
    produit_description = produit['product']['product_name']
    produit_grade_tag = produit['product']['nutrition_grades_tags']
    produit_status = produit['status']
    if produit_status == '1':
        produit_status = 'valide'
    result_dict = {
        'produit_name': produit_name,
        'produit_description': produit_description,
        'produit_grade_tag': produit_grade_tag,
        'produit_status': produit_status
    }
    result_json = jsonify(result_dict)
    return result_json

if __name__ == '__main__':
    getproduct()