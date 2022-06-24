import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls.Material 2.3
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3
import QtQuick.Controls.Styles 1.4
import QtGraphicalEffects 1.15
import QtQuick.Shapes 1.15
import QtQuick.Extras 1.4

Item{
    id: myButton
    Layout.preferredWidth: parent.width
    Layout.preferredHeight: parent.width / 2
    Layout.alignment: Qt.AlignCenter
    property var settext
    Button{
        id: nextRound
        anchors.fill: parent
        text: settext
        font.bold: true
        font.pixelSize: 15
        background : Rectangle{
          anchors.fill: parent
          color: "#325c32"
        }
    }
}