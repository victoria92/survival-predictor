class ClassWithNoImportanceProvided(Exception):
    pass


class KNearestNeighbours():
    """
    Provide instance of this class with data, afterwards
    simply use determine_survival and it will return result
    depending on whether
    """
    def __init__(self, data, k=15):
        self.data = data
        self.classes = [
            'pclass', 'name', 'sex', 'age', 'sibsp', 'parch',
            'ticket', 'fare', 'cabin', 'embarked'
        ]
        self.classes_importance = self.classes_importance_determination()
        self.k = k  # the number of the closest neighbours to consider

    def classes_importance_determination(self):
        importances = {
            'pclass': 1,   # passenger class
            'name': 0,     # name of the passange
            'sex': 0.6,    # female / male
            'age': 0.8,    # age
            'sibsp': 0.5,  # number of siblings/spouses aboard
            'parch': 0.7,  # number of parents/children aboard
            'ticket': 0,   # ticket number
            'fare': 0.4,   # passenger fare paid for the travel
            'cabin': 0.9,  # cabin number
            'embarked': 0  # port of embarkation
        }

        if any(_class not in importances for _class in self.classes):
            raise ClassWithNoImportanceProvided

        return importances

    def will_survive(self, passenger_variables):
        """
        Given the passenger variables determine if he will survive or not
        depending on the self.data populated
        """
        similarity = []
        for passenger in self.data:
            similarity.append(
                self.passengers_similarity(passenger_variables, passenger)
            )

        survival_of_kneighbours = [
            neighbour[0] for neighbour in
            sorted(similarity, key=lambda tpl: tpl[1])[-self.k:]
        ]

        if survival_of_kneighbours.count(0) > survival_of_kneighbours.count(1):
            return False
        return True

    def passengers_similarity(self, unknown_passenger, known_passenger):
        """
        Given two passangers (one unknown if has survived)
        returns tuple of this kind: (1/0, similarity_score)

        First item is if the known_passenger has survived
        """
        similarity_score = 0
        for clss in self.classes:
            if self.accumulate_class(clss, unknown_passenger, known_passenger):
                similarity_score += self.classes_importance[clss]

        return (int(known_passenger['survived']), round(similarity_score, 2))

    def accumulate_class(self, class_name, unknown_passenger, known_passenger):
        """
        True / False depending on if the class importance
        should be taken into consideration

        unknown_passenger and known_passenger are dict type
        """
        if self.classes_importance[class_name] == 0:
            return False

        return getattr(
            self.__class__,
            class_name
        )(unknown_passenger, known_passenger)

    def age(unknown_passenger, known_passenger):
        """ True if both passangers are close at age """
        if (
            unknown_passenger['age'] and known_passenger['age'] and
            abs(float(unknown_passenger['age']) - float(known_passenger['age'])) < 10
        ):
            return True
        return False

    def pclass(unknown_passenger, known_passenger):
        """ True if both passangers same pclass """
        if unknown_passenger['pclass'] == known_passenger['pclass']:
            return True
        return False

    def sex(unknown_passenger, known_passenger):
        """ True if both passangers same gender """
        if unknown_passenger['sex'] == known_passenger['sex']:
            return True
        return False

    def sibsp(unknown_passenger, known_passenger):
        """ True if both passangers same number of siblings count """
        if unknown_passenger['sibsp'] == known_passenger['sibsp']:
            return True
        return False

    def parch(unknown_passenger, known_passenger):
        """ True if both passangers same parrents / children count """
        if unknown_passenger['parch'] == known_passenger['parch']:
            return True
        return False

    def fare(unknown_passenger, known_passenger):
        """ True if both passangers have paid close fares """
        if (
            unknown_passenger['fare'] and known_passenger['fare'] and
            abs(float(unknown_passenger['fare']) - float(known_passenger['fare'])) < 15
        ):
            return True
        return False

    def cabin(unknown_passenger, known_passenger):
        """ True if both passangers in same cabin """
        if unknown_passenger['cabin'] == known_passenger['cabin']:
            return True
        return False
