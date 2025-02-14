from config.db import machinesCollection
from bson import ObjectId

class MachineController:
    def insertMachine(machineData):
        result = machinesCollection.insert_one(machineData)
        machineData["id"] = str(result.inserted_id)
        return machineData

    def getMachineById(machineID):
        if not ObjectId.is_valid(machineID):
            return None

        machine = machinesCollection.find_one({"_id": ObjectId(machineID)})
        if machine:
            machine["id"] = str(machine["_id"])
            del machine["_id"]
        return machine

    def updateMachineById(machineID , machineData):
        if not ObjectId.is_valid(machineID):
            return None

        updatedMachine = machinesCollection.find_one_and_update(
            {"_id": ObjectId(machineID)},
            {"$set": machineData},
            return_document=True
        )
        if updatedMachine:
            updatedMachine["id"] = str(updatedMachine["_id"])
            del updatedMachine["_id"]
        return updatedMachine

    def deleteMachineById(machineID):
        if not ObjectId.is_valid(machineID):
            return None
        
        return machinesCollection.find_one_and_delete({"_id": ObjectId(machineID)})
    
    def getAllMachines():
        machines = list(machinesCollection.find())
        for machine in machines:
            machine["id"] = str(machine["_id"])
            del machine["_id"]
        return machines
