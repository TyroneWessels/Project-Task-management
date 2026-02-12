#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Project_manager import ProjectManager
from Task_manager import TaskManager
from Storage import StorageManager

def test_filter_functionality():
    """Test de filter functionaliteit"""
    print("=== TEST FILTER TAKEN OP STATUS ===\n")
    
    # Setup
    storage = StorageManager()
    pm = ProjectManager(storage)
    tm = TaskManager(storage)
    
    # Maak test project
    succes, bericht, project = pm.maak_project_aan('Test Project', 'Test beschrijving')
    print(f'Project aangemaakt: {succes} - {bericht}')
    
    if not succes:
        print("Kan niet verder testen zonder project")
        return
    
    # Maak test taken
    taken_data = [
        ('Taak 1', 'Nieuwe taak', 'normaal'),
        ('Taak 2', 'Bezige taak', 'hoog'), 
        ('Taak 3', 'Afgeronde taak', 'laag')
    ]
    
    for titel, beschrijving, prioriteit in taken_data:
        succes, bericht, taak = tm.maak_taak_aan(project, titel, beschrijving, prioriteit)
        print(f'Taak aangemaakt: {succes} - {bericht}')
    
    # Wijzig statussen
    print('\n--- Statussen wijzigen ---')
    tm.wijzig_taakstatus(project, 'Taak 2', 'bezig')
    tm.wijzig_taakstatus(project, 'Taak 3', 'afgerond')
    
    # Test filter op status
    print('\n=== FILTER TESTS ===')
    
    print('\n1. Filter op NIEUW:')
    resultaat = tm.filter_taken_op_status(project, 'nieuw')
    print(resultaat)
    
    print('\n2. Filter op BEZIG:')
    resultaat = tm.filter_taken_op_status(project, 'bezig')
    print(resultaat)
    
    print('\n3. Filter op AFGEROND:')
    resultaat = tm.filter_taken_op_status(project, 'afgerond')
    print(resultaat)
    
    print('\n4. Filter ongeldige status:')
    resultaat = tm.filter_taken_op_status(project, 'ongeldig')
    print(resultaat)
    
    print('\n=== TEST COMPLEET ===')

if __name__ == "__main__":
    test_filter_functionality()
