#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Project_manager import ProjectManager
from Task_manager import TaskManager
from Storage import StorageManager

def test_complete_functionality():
    """Test alle functionaliteit inclusief correcte statusovergangen"""
    print("=== COMPLETE FUNCTIONALITEIT TEST ===\n")
    
    # Setup
    storage = StorageManager()
    pm = ProjectManager(storage)
    tm = TaskManager(storage)
    
    # 1. Project aanmaken
    print("1. PROJECT AANMAKEN")
    succes, bericht, project = pm.maak_project_aan('Test Project', 'Test beschrijving')
    print(f'   Resultaat: {succes} - {bericht}')
    
    # 2. Taken aanmaken
    print("\n2. TAKEN AANMAKEN")
    taken_data = [
        ('Taak Nieuw', 'Nieuwe taak', 'normaal'),
        ('Taak Bezig', 'Taak die bezig is', 'hoog'), 
        ('Taak Afgerond', 'Taak die afgerond wordt', 'laag')
    ]
    
    for titel, beschrijving, prioriteit in taken_data:
        succes, bericht, taak = tm.maak_taak_aan(project, titel, beschrijving, prioriteit)
        print(f'   {titel}: {succes} - {bericht}')
    
    # 3. Status wijzigen (correcte overgangen)
    print("\n3. STATUS WIJZIGEN")
    
    # Taak Bezig: nieuw → bezig
    succes, bericht = tm.wijzig_taakstatus(project, 'Taak Bezig', 'bezig')
    print(f'   Taak Bezig → bezig: {succes} - {bericht}')
    
    # Taak Afgerond: nieuw → bezig → afgerond
    succes, bericht = tm.wijzig_taakstatus(project, 'Taak Afgerond', 'bezig')
    print(f'   Taak Afgerond → bezig: {succes} - {bericht}')
    
    succes, bericht = tm.wijzig_taakstatus(project, 'Taak Afgerond', 'afgerond')
    print(f'   Taak Afgerond → afgerond: {succes} - {bericht}')
    
    # 4. Filter op status
    print("\n4. FILTER TAKEN OP STATUS")
    
    for status in ['nieuw', 'bezig', 'afgerond']:
        print(f'\n   Filter op {status}:')
        resultaat = tm.filter_taken_op_status(project, status)
        print(f'   Aantal gevonden: {resultaat.count("ta(a)k(en)") > 0}')
    
    # 5. Zoekfunctie (bestaande)
    print("\n5. ZOEKFUNCTIE")
    taak = tm.zoek_taak(project, 'Taak Bezig')
    print(f'   Taak zoeken: {"Gevonden" if taak else "Niet gevonden"}')
    
    # 6. Projectoverzicht
    print("\n6. PROJECTOVERZICHT")
    overzicht = pm.toon_projectoverzicht()
    print(f'   Projectoverzicht: {"Succes" if "Test Project" in overzicht else "Mislukt"}')
    
    # 7. Taakdetails
    print("\n7. TAAKDETAILS")
    details = tm.toon_taakdetails(project, 'Taak Afgerond')
    print(f'   Taakdetails: {"Succes" if "Taak Afgerond" in details else "Mislukt"}')
    
    # 8. Validatie tests
    print("\n8. VALIDATIE TESTS")
    
    # Probeer dubbele projectnaam
    succes, bericht, _ = pm.maak_project_aan('Test Project', 'Dubbel project')
    print(f'   Dubbele projectnaam: {"Geblokkeerd" if not succes else "Toegelaten"}')
    
    # Probeer taak in gesloten project
    project.sluit_project()
    succes, bericht, _ = tm.maak_taak_aan(project, 'Nieuwe taak', 'Test', 'normaal')
    print(f'   Taak in gesloten project: {"Geblokkeerd" if not succes else "Toegelaten"}')
    
    print("\n=== TEST COMPLEET ===")

if __name__ == "__main__":
    test_complete_functionality()
