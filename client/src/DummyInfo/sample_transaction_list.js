const sample_transaction_list = [
    {
        payer_name: "Jessica",
        total: 600,
        expected_cost: {"Jessica": 200, 
                        "Julia": 400, 
                        "Max": 0, 
                        "Anderson": 0,
                        "Esther": 0},
        title : "8/11 Lunch",
        description : "hotpot: Jessica and Julia"
    },
    {
        payer_name: "Max",
        total: 700,
        expected_cost: {"Jessica": 0, 
                        "Julia": 0, 
                        "Max": 350, 
                        "Anderson": 350,
                        "Esther": 0},
        title : "8/11 Lunch",
        description : "hotpot: Max and Anderson"
    },
    {
        payer_name: "Esther",
        total: 300,
        expected_cost: {"Jessica": 0, 
                        "Julia": 0, 
                        "Max": 0, 
                        "Anderson": 0,
                        "Esther": 300},
        title : "8/11 Lunch",
        description : "hotpot: Esther"
    }
]
/*
Cost fields:
    payer : Member
    The person who pays the total in this cost event
    total : float
    The total amount in this cost event
    expected_cost : dict
    (k, v) = (person, the amount he/she has to pay)
    title : str
    The title of this cost
    description : str
    tag : str
*/