import json
import requests

def getproduct(code_barre):
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
        'produit_name': str(produit_name),
        'produit_description': str(produit_description),
        'produit_grade_tag': str(produit_grade_tag),
        'produit_status': str(produit_status)
    }
    result_json = json.dumps(result_dict)
    return result_json

if __name__ == '__main__':
    getproduct()
