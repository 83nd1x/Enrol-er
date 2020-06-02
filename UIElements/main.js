function letTheBotOut() {
    //user input
    var datadwsurl = document.getElementById('dwsurl').value
    var dataduxp = document.getElementById('duxp').value
    var datadpxp = document.getElementById('dpxp').value
    var datadlbxp = document.getElementById('dlbxp').value
    var datadu = document.getElementById('du').value
    var datadp = document.getElementById('dp').value
    var datadtime = document.getElementById('dtime').value
    var datadfurl = document.getElementById('dfurl').value
    var datadfbxp = document.getElementById('dfbxp').value
    //to python
    eel.letTheBotOut(datadwsurl, dataduxp, datadpxp, datadlbxp, datadu, datadp, datadtime, datadfurl, datadfbxp)
    //eel.letTheBotOut(dataduxp)
    //eel.letTheBotOut(datadpxp)
    //eel.letTheBotOut(datadlbxp)
    //eel.letTheBotOut(datadu)
    //eel.letTheBotOut(datadp)
    //eel.letTheBotOut(datadtime)
    //eel.letTheBotOut(datadfurl)
    //eel.letTheBotOut(datadfbxp)
    //python code
    eel.letTheBotOut("this is eel")(function(ret) {console.log(ret)})
}