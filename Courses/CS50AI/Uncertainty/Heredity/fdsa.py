    mother_gene = Categorical(
            [PROBS["gene"][0],PROBS["gene"][1],PROBS["gene"][2]], 
            [0,1,2]
            )

    mother_trait = ConditionalCategorical([
        [PROBS["trait"][0][True], PROBS["trait"][0][False]], #Trait is true given gene is 0
        [PROBS["trait"][1][True], PROBS["trait"][1][False]], 
        [PROBS["trait"][2][True],PROBS["trait"][2][False]], 
    ], states = [True, False], parents = [mother_gene])

    father_gene = Categorical(
            [PROBS["gene"][0],PROBS["gene"][1],PROBS["gene"][2]], 
            [0,1,2]
            )
    
    father_trait = ConditionalCategorical([
        [PROBS["trait"][0][True], PROBS["trait"][0][False]], #Trait is true given gene is 0
        [PROBS["trait"][1][True], PROBS["trait"][1][False]], 
        [PROBS["trait"][2][True],PROBS["trait"][2][False]], 
    ], states = [True, False], parents = [father_gene])

    # child_gene = ConditionalCategorical([
    #     [PROBS["mutation"] * PROBS["mutation"], 1 - PROBS["mutation"] * PROBS["mutation"]],                 #Gene is mutated when copy in mother and father is 0
    #     [PROBS["mutation"] * 0.5, 1 - PROBS["mutation"] * 0.5],                                             #Gene is mutataed when the copy in mother is 0 and father is 1
    #     [PROBS["mutation"] * (1 - PROBS["mutation"]), 1 - PROBS["mutation"] * (1 - PROBS["mutation"])],     #Mother -0, Father -2 
    #     [0.5 * PROBS["mutation"], 1 - 0.5 * PROBS["mutation"]],                                             #Mother -1, Father -0 
    #     [0.5 * 0.5, 1 - 0.5 * 0.5],                                                                         #Mother -1, Father - 1 
    #     [0.5 * (1-PROBS["mutation"]), 1 - 0.5 * (1-PROBS["mutation"])],                                     #Mother -1, Father - 2
    #     [(1-PROBS["mutation"]) * PROBS["mutation"], 1 - (1-PROBS["mutation"]) * PROBS["mutation"]],         #Mother -2, Father - 0
    #     [(1-PROBS["mutation"]) * 0.5, 1 - (1-PROBS["mutation"]) * 0.5],                                     #Mother -2, Father - 1
    #     [(1-PROBS["mutation"]) * (1-PROBS["mutation"]), 1 - (1-PROBS["mutation"])* (1-PROBS["mutation"])],  #Mother -2, Father - 2
    # ], states = [0,1,2], parents = [mother_gene, father_gene])

    child_gene = ConditionalCategorical([
        [PROBS["mutation"] * PROBS["mutation"], 1 - PROBS["mutation"] * PROBS["mutation"]],                 #Gene is mutated when copy in mother and father is 0
        [PROBS["mutation"] * 0.5, 1 - PROBS["mutation"] * 0.5],                                             #Gene is mutataed when the copy in mother is 0 and father is 1
        [PROBS["mutation"] * (1 - PROBS["mutation"]), 1 - PROBS["mutation"] * (1 - PROBS["mutation"])],     #Mother -0, Father -2 
        [0.5 * PROBS["mutation"], 1 - 0.5 * PROBS["mutation"]],                                             #Mother -1, Father -0 
        [0.5 * 0.5, 1 - 0.5 * 0.5],                                                                         #Mother -1, Father - 1 
        [0.5 * (1-PROBS["mutation"]), 1 - 0.5 * (1-PROBS["mutation"])],                                     #Mother -1, Father - 2
        [(1-PROBS["mutation"]) * PROBS["mutation"], 1 - (1-PROBS["mutation"]) * PROBS["mutation"]],         #Mother -2, Father - 0
        [(1-PROBS["mutation"]) * 0.5, 1 - (1-PROBS["mutation"]) * 0.5],                                     #Mother -2, Father - 1
        [(1-PROBS["mutation"]) * (1-PROBS["mutation"]), 1 - (1-PROBS["mutation"])* (1-PROBS["mutation"])],  #Mother -2, Father - 2
    ], states = [0,1,2], parents = [mother_gene, father_gene])

    child_trait = ConditionalCategorical([
        [PROBS["trait"][0][True], PROBS["trait"][0][False]], #Trait is true given gene is 0
        [PROBS["trait"][1][True], PROBS["trait"][1][False]], 
        [PROBS["trait"][2][True],PROBS["trait"][2][False]], 
    ], states = [True, False], parents = [child_gene])