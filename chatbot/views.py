from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from menu.models import Plat
from restaurant.models import Table
from orders.models import Commande


class ChatbotView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return render(request, 'chatbot/chat.html')


class ChatbotResponseView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        user_message = request.data.get('message', '').lower()
        response = self.process_user_message(user_message)
        return Response({'response': response})
    
    def process_user_message(self, message):
        plats_disponibles = Plat.objects.filter(disponible=True)
        tables_disponibles = Table.objects.filter(est_occupee=False)
        
        if 'menu' in message or 'plats' in message or 'que proposez-vous' in message:
            return self.afficher_menu(plats_disponibles)
        elif 'commander' in message or 'je veux' in message or 'je prendrai' in message:
            return self.traiter_commande(message, plats_disponibles)
        elif 'tables' in message or 'table' in message:
            return self.afficher_tables(tables_disponibles)
        elif 'bonjour' in message or 'salut' in message:
            return "Bonjour ! Comment puis-je vous aider aujourd'hui ? Je peux vous montrer le menu, prendre votre commande ou vous indiquer les tables disponibles."
        elif 'merci' in message:
            return "De rien ! Bon appétit !"
        else:
            return "Désolé, je ne comprends pas. Pouvez-vous reformuler ? Je peux vous aider avec le menu, les commandes ou les tables."
    
    def afficher_menu(self, plats):
        if not plats:
            return "Désolé, il n'y a pas de plats disponibles pour le moment."
        
        menu_text = "Voici notre menu :\n"
        for plat in plats:
            menu_text += f"- {plat.nom} : {plat.prix} DH\n"
            if plat.description:
                menu_text += f"  {plat.description}\n"
        menu_text += "\nQue voulez-vous commander ?"
        return menu_text
    
    def traiter_commande(self, message, plats):
        plats_commandes = []
        
        for plat in plats:
            if plat.nom.lower() in message:
                plats_commandes.append(plat)
        
        if not plats_commandes:
            return "Désolé, je n'ai pas trouvé ces plats dans notre menu. Pouvez-vous préciser ?"
        
        table_numero = self.extraire_numero_table(message)
        
        if not table_numero:
            return "Pour quelle table voulez-vous commander ? Veuillez préciser le numéro de table (ex: Table 1)."
        
        try:
            table = Table.objects.get(numero=table_numero)
        except Table.DoesNotExist:
            return f"La table {table_numero} n'existe pas. Veuillez vérifier le numéro."
        
        commande = Commande.objects.create(table=table)
        commande.plats.add(*plats_commandes)
        
        total = sum(plat.prix for plat in plats_commandes)
        commande.total = total
        commande.save()
        
        plats_noms = ', '.join([plat.nom for plat in plats_commandes])
        return f"Parfait ! J'ai enregistré votre commande pour la table {table_numero} : {plats_noms}. Total : {total} DH. Bon appétit !"
    
    def extraire_numero_table(self, message):
        mots = message.split()
        for i, mot in enumerate(mots):
            if 'table' in mot and i + 1 < len(mots):
                try:
                    return int(mots[i + 1])
                except ValueError:
                    continue
            if mot.isdigit():
                return int(mot)
        return None
    
    def afficher_tables(self, tables):
        if not tables:
            return "Désolé, toutes les tables sont occupées pour le moment."
        
        tables_text = "Voici les tables disponibles :\n"
        for table in tables:
            tables_text += f"- Table {table.numero} (capacité: {table.capacite} personnes)\n"
        return tables_text
