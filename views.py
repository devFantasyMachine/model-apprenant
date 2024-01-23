from .models import concept, subconcept, evidence
import pyAgrum as gum

def create_bayesian_network():
    model = gum.BayesNet("Learner's Knowledge Model")
    concepts = concept.objets.all()

    nodes = {}
    for Concept in concepts:
        model.add(Concept)

    for Concept in concepts:
        for child in Concept.subconcepts:
            Subconcept = subconcept.objects.get(subconcept_id = child)
            model.add(subconcept)
            model.addArc(Concept, Subconcept)
            for symptoms in Subconcept.evidences:
                Evidence = evidence.objects.get(evidence_id= symptoms)
                model.add(Evidence)
                model.addArc(Subconcept, Evidence)

    concept_init_prob = {'True': 0.5, 'False': 0.5}
    subconcept_init_prob = {'True': 0.6, 'False': 0.4}
    evidence_init_prob = {'True': 0.8, 'False': 0.2}

    for node in model.nodes:
        if node.name.startswith('Concept'):
            node.cpt = model.cpt(node).fillWith([(concept_init_prob,)])
        if node.name.startswith('SubConcept'):
            node.cpt = model.cpt(node).fillWith([(subconcept_init_prob)])
        if node.name.startswith('evidence'):
            node.cpt = model.cpt(node).fillWith([(evidence_init_prob)])

    return model

