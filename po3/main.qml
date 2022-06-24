import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.3
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.15
import QtQuick.Shapes 1.15
import QtQuick.Extras 1.4

ApplicationWindow {
  id: app
  flags: Qt.Window
  width: 1000
  visible: true
  height: 800
  title: "krzys"
  background : Rectangle{
      anchors.fill: parent
      color: "#0f140f"
    }
  Pane{
    anchors.fill: parent
    focus: true
    padding: 0
    Keys.onPressed:{
      switch(event.key){
        case Qt.Key_Up:
          Get.HumanDir("Up")
          break;
        case Qt.Key_Down:
          Get.HumanDir("Down")
          break;
        case Qt.Key_Left:
          Get.HumanDir("Left")
          break;
        case Qt.Key_Right:
          Get.HumanDir("Right")
          break;
        case Qt.Key_Space:
          Get.HumanDir("Ability")
      }
    }
  Pane{
    z:1
    id: log
    implicitWidth: 200
    implicitHeight: parent.height
    anchors.left : parent.left
    padding: 30
    background : Rectangle{
      anchors.fill: parent
      color: "#0f140f"
    }
    ListView{
      id: logView
      anchors.fill: parent
      model: logModel
      delegate: Text{
        text: model.text
        color: "#ccca49"
      }
    }
  }
  Pane{
    z:2
    id: rightMenu
    implicitWidth: 200
    implicitHeight: parent.height
    anchors.right : parent.right
    background : Rectangle{
      anchors.fill: parent
      color: "#0f140f"
    }
    Rectangle{
      anchors.fill: parent
      color: "#192119"
    }
    ColumnLayout{
      width: parent.width / 2
      height: parent.height
      anchors.horizontalCenter : parent.horizontalCenter
      MyButton{
        settext: "Next"
        MouseArea{
          anchors.fill: parent
          onClicked: Get.Next()
        }
      }
      MyButton{
        settext: "Save"
        MouseArea{
          anchors.fill: parent
          onClicked: Get.Save()
        }
      }
      MyButton{
        settext: "Load"
        MouseArea{
          anchors.fill: parent
          onClicked: Get.Load()
        }
      }
    }
  }
  Pane{
      id: map
      width: parent.width - rightMenu.width -log.width
      height: parent.height
      z: 0
      background : Rectangle{
        anchors.fill: parent
        color: "#0f140f"
      }
      anchors.left: log.right
      GridLayout{
        id: grid
        rowSpacing: 2
        columnSpacing: 2
        anchors.centerIn: parent
        Repeater{
          model:mapModel
          delegate:Rectangle{
            height: model.height
            width: model.width
            color: model.color
            MouseArea{
              anchors.fill:parent
              onClicked: {
                contextMenu.idefix = index
                contextMenu.popup()
              }
            }
          }
        }
      }

    }
  ListModel{
    id:mapModel
  }

  ListModel{
    id:logModel
  }

  Menu {
        id: contextMenu
        property var idefix: -1
        MenuItem { 
          text: "Sheep"
          onClicked: Get.NewOrganism(contextMenu.idefix,"Sheep")
        }
        MenuItem { 
          text: "Wolf"
          onClicked: Get.NewOrganism(contextMenu.idefix,"Wolf")
        }
        MenuItem { 
          text: "Turtle"
          onClicked: Get.NewOrganism(contextMenu.idefix,"Turtle")
        }
        MenuItem { 
          text: "Fox"
          onClicked: Get.NewOrganism(contextMenu.idefix,"Fox")
        }
        MenuItem { 
          text: "Antelope"
          onClicked: Get.NewOrganism(contextMenu.idefix,"Antelope")
        }
        MenuItem { 
          text: "CyberSheep"
          onClicked: Get.NewOrganism(contextMenu.idefix,"CyberSheep")
        }
        MenuItem { 
          text: "Grass"
          onClicked: Get.NewOrganism(contextMenu.idefix,"Grass")
        }
        MenuItem { 
          text: "Dandelion"
          onClicked: Get.NewOrganism(contextMenu.idefix,"Dandelion")
        }
        MenuItem { 
          text: "Guarana"
          onClicked: Get.NewOrganism(contextMenu.idefix,"Guarana")
        }
        MenuItem { 
          text: "Nightshade"
          onClicked: Get.NewOrganism(contextMenu.idefix,"Nightshade")
        }
        MenuItem { 
          text: "Hogweed"
          onClicked: Get.NewOrganism(contextMenu.idefix,"Hogweed")
        }
    }
  }

  property var objects:({log:log, map:map, mapModel:mapModel, grid: grid})
  function getElement(str)
    {return objects[str]}
  function addToList(element){
    mapModel.append(element)
  }
  function clearList(){
    mapModel.clear()
  }
  function addToLog(str){
    logModel.insert(0,str)
  }
}