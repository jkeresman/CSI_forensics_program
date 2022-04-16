from deepdiff import DeepDiff

human_characteristics = {

    "hair_color": {
        "black": "CCAGCAATCGC",
        "brown": "GCCAGTGCCG",
        "blonde": "TTAGCTATCGC",
    },

    "facial_shape": {
        "square": "GCCACGG",
        "round": "ACCACAA",
        "oval": "AGGCCTCA",
    },

    "eye_color": {
        "blue": "TTGTGGTGGC",
        "green": "GGGAGGTGGC",
        "brown": "AAGTAGTGAC",
    },

    "gender": {
        "female": "TGAAGGACCTTC",
        "male": "TGCAGGAACTTC",
    },

    "race": {
        "white": "AAAACCTCA",
        "black": "CGACTACAG",
        "asian": "CGCGGGCCG",
    }

}

suspects = [

    {
        "name": "Eva",
        "gender": "female",
        "race": "white",
        "hair_color": "blonde",
        "eye_color": "blue",
        "facial_shape": "oval",
    },

    {
        "name": "Larisa",
        "gender": "female",
        "race": "white",
        "hair_color": "brown",
        "eye_color": "brown",
        "facial_shape": "oval",
    },

    {
        "name": "Matej",
        "gender": "male",
        "race": "white",
        "hair_color": "black",
        "eye_color": "blue",
        "facial_shape": "oval",
    },

    {
        "name": "Miha",
        "gender": "male",
        "race": "white",
        "hair_color": "brown",
        "eye_color": "green",
        "facial_shape": "square",
    }

]

perpetrator = {}
perpetrator_name = ""

with open("dna.txt", "r") as dna_file:
    dna_sequence = dna_file.read()


for human_characteristic, value in human_characteristics.items():
    for characteristic_value, sequence in value.items():
        if dna_sequence.find(sequence) != -1:
            perpetrator[human_characteristic] = characteristic_value
            break

for suspect in suspects:
    suspect_perpetrator_diff = DeepDiff(suspect, perpetrator)
    if len(suspect_perpetrator_diff) == 1:
        perpetrator_name = suspect["name"]

print(f"Perpetrator is {perpetrator_name}")
