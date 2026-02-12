#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Project_manager import ProjectManager
from Task_manager import TaskManager
from Storage import StorageManager

def debug_taak3_status():
    """Debug de status van Taak 3"""
    print("=== DEBUG TAAK 3 STATUS ===\n")
    
    # Setup
    storage = StorageManager()
    pm = ProjectManager(storage)
    tm = TaskManager(storage)
    
    # Maak test project
    succes, bericht, project = pm.maak_project_aan('Debug Project', 'Test beschrijving')
    print(f'Project aangemaakt: {succes}')
    
    # Maak Taak 3
    succes, bericht, taak = tm.maak_taak_aan(project, 'Taak 3', 'Test taak', 'laag')
    print(f'Taak 3 aangemaakt: {succes}')
    
    print(f'\nStatus voor wijziging: {taak.status.value}')
    
    # Wijzig naar afgerond
    succes, bericht = tm.wijzig_taakstatus(project, 'Taak 3', 'afgerond')
    print(f'Status wijziging: {succes} - {bericht}')
    
    # Controleer status direct
    print(f'Status na wijziging: {taak.status.value}')
    if taak.afrondmoment:
        print(f'Afrondmoment: {taak.afrondmoment}')
    
    # Filter op afgerond
    print('\nFilter resultaat:')
    resultaat = tm.filter_taken_op_status(project, 'afgerond')
    print(resultaat)
    
    # Toon alle taken
    print('\nAlle taken in project:')
    for i, t in enumerate(project.tasks):
        print(f'Taak {i+1}: {t.titel} - Status: {t.status.value}')

if __name__ == "__main__":
    debug_taak3_status()
