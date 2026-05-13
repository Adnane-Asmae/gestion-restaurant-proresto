from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from restaurant.models import Table
from menu.models import Plat
from .models import Commande


class CommandeTest(TestCase):

    def test_creation_commande(self):

        table = Table.objects.create(
            numero=1,
            capacite=4
        )

        commande = Commande.objects.create(
            table=table
        )

        self.assertEqual(
            commande.table.numero,
            1
        )


    def test_calcul_total(self):

        table = Table.objects.create(
            numero=2,
            capacite=4
        )

        plat = Plat.objects.create(
            nom='Pizza',
            prix=50
        )

        commande = Commande.objects.create(
            table=table
        )

        commande.plats.add(plat)

        commande.calculate_total()

        self.assertEqual(
            commande.total,
            50
        )