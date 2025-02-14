from fastapi import APIRouter, HTTPException
from model import Machine
from controller import MachineController

router = APIRouter()

@router.post("/machines/create-machine")
def createMachine(machine: Machine):
    machineDictionary = machine.model_dump()     # Convert the machine object to a dictionary
    insertedMachine = MachineController.insertMachine(machineDictionary)
    if not insertedMachine:
        raise HTTPException(status_code=400, detail="Failed to create machine")
    print(f"Machine created successfully with id: {insertedMachine['id']}")
    return insertedMachine

@router.get("/machines/all-machines")
def getAllMachines():
    machines = MachineController.getAllMachines()
    return machines

@router.get("/machines/{machineId}")
def getMachine(machineId: str):
    machine = MachineController.getMachineById(machineId)
    if not machine:
        raise HTTPException(status_code=404, detail="Machine not found")
    return machine

@router.put("/machines/{machineId}")
def updateMachine(machineId: str, machineData: Machine):
    updatedMachine = MachineController.updateMachineById(machineId, machineData.model_dump())
    if not updatedMachine:
        raise HTTPException(status_code=404, detail="Machine not found")
    return updatedMachine

@router.delete("/machines/{machineId}")
def deleteMachine(machineId: str):
    deletedMachine = MachineController.deleteMachineById(machineId)
    if not deletedMachine:
        raise HTTPException(status_code=404, detail="Machine not found")
    return {"message": "Machine deleted successfully", "deletedMachineId": machineId}

