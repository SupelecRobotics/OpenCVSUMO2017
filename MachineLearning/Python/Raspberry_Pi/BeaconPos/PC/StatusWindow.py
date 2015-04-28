import numpy as np
import cv2

NB_ROB_TYPES = 4

class StatusWindow:

    def __init__(self, beaconPos):

        self.beaconPos = beaconPos
        self.selectedRobType = 0
        self.selectedRefPoint = 0
        self.refPoints = []

        self.STATUS_ZONE_H = 50
        self.tablePic = cv2.imread('schema_table2.png')
        cv2.namedWindow('Status')

    def update(self):

        h,w = self.tablePic.shape[:2]
        
        frame = np.zeros((h + self.STATUS_ZONE_H, w, 3), np.uint8)

        if(self.beaconPos.isConnected()):
            cv2.putText(frame, 'LAN connected', (0,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        else:
            cv2.putText(frame, 'LAN disconnected', (0,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.putText(frame, 'Selected bot type : ' + str(self.selectedRobType), (0,45), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))

        frame[self.STATUS_ZONE_H:] = self.tablePic

        for i in range(0, len(self.refPoints)):
            point = self.refPoints[i]
            if(i == self.selectedRefPoint):
                cv2.circle(frame,(point[0],point[1]+self.STATUS_ZONE_H),5,(255,255,255),2)
            else:
                cv2.circle(frame,(point[0],point[1]+self.STATUS_ZONE_H),5,(255,0,0),2)

        
        cv2.imshow('Status',frame)

    def selectNextRobType(self):

        if(self.selectedRobType == NB_ROB_TYPES-1):
            self.selectedRobType = 0
        else:
            self.selectedRobType = self.selectedRobType + 1

    def selectPrevRobType(self):

        if(self.selectedRobType == 0):
            self.selectedRobType = NB_ROB_TYPES-1
        else:
            self.selectedRobType = self.selectedRobType - 1

    def selectNextRefPoint(self):

        if(self.selectedRefPoint == len(self.refPoints)-1):
            self.selectedRefPoint = 0
        else:
            self.selectedRefPoint = self.selectedRefPoint + 1

    def selectPrevRefPoint(self):

        if(self.selectedRefPoint == 0):
            self.selectedRefPoint = len(self.refPoints)-1
        else:
            self.selectedRefPoint = self.selectedRefPoint - 1

    def setRefPoints(self, refPoints):

        self.refPoints = refPoints

    def getSelectedRobType(self):

        return self.selectedRobType

    def getRefPoints(self):

        return list(self.refPoints)

    def getSelectedRefPoint(self):

        return self.selectedRefPoint