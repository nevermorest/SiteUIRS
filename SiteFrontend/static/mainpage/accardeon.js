function changecolor(title){
    let aboba = document.getElementById(title)
    if(aboba.style.display == "block"){
        aboba.style.display = "none"
    }else{
        aboba.style.display = "block"
    }
    
}

function showFiltersVideoCard(){ //пишешь функцию с нужным пресетом, вызываешь на он клик в id="details_dropdown_content"
    const preset =["prod_section", "price_section", "videoMem_section","busSize_section","prodGPU_section","monitorConSize_section"]
    let allNodes = document.getElementById("filter_border").childNodes;
    for(var i = 0; i < allNodes.length; i++) {
        if(allNodes[i].nodeType == 1){
            if(preset.some(el => el == allNodes[i].id)){
                allNodes[i].childNodes.forEach(el => {
                    if(el.nodeType == 1){
                        console.log(el)
                        el.style.display = "block"
                    }
                })
            }else{
                allNodes[i].childNodes.forEach(el => {
                    if(el.nodeType == 1){
                        console.log(el)
                        el.style.display = "none"
                    }
                })
            }
        }
        
    }
}
function showFiltersMother(){ //пишешь функцию с нужным пресетом, вызываешь на он клик в id="details_dropdown_content"
    const preset =["prod_section", "price_section","chipset_section", "socket_section","memoryTypeCpn_section","memorySlotSize_section","memoryM2Size_section"]
    let allNodes = document.getElementById("filter_border").childNodes;
    for(var i = 0; i < allNodes.length; i++) {
        if(allNodes[i].nodeType == 1){
            if(preset.some(el => el == allNodes[i].id)){
                allNodes[i].childNodes.forEach(el => {
                    if(el.nodeType == 1){
                        console.log(el)
                        el.style.display = "block"
                    }
                })
            }else{
                allNodes[i].childNodes.forEach(el => {
                    if(el.nodeType == 1){
                        console.log(el)
                        el.style.display = "none"
                    }
                })
            }
        }
        
    }
}
function showCPFilters(){ //пишешь функцию с нужным пресетом, вызываешь на он клик в id="details_dropdown_content"
    const preset =["prod_section", "price_section","socket_section","cpuCores_section","memoryType_section"]
    let allNodes = document.getElementById("filter_border").childNodes;
    for(var i = 0; i < allNodes.length; i++) {
        if(allNodes[i].nodeType == 1){
            if(preset.some(el => el == allNodes[i].id)){
                allNodes[i].childNodes.forEach(el => {
                    if(el.nodeType == 1){
                        console.log(el)
                        el.style.display = "block"
                    }
                })
            }else{
                allNodes[i].childNodes.forEach(el => {
                    if(el.nodeType == 1){
                        console.log(el)
                        el.style.display = "none"
                    }
                })
            }
        }
        
    }
}