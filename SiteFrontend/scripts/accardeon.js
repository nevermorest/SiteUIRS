function changecolor(title) {
    let aboba = document.getElementById(title);
    aboba.style.display = (aboba.style.display === "block") ? "none" : "block";
}

function showFilters(preset) {
    let allNodes = document.getElementById("filter_border").childNodes;
    for (var i = 0; i < allNodes.length; i++) {
        if (allNodes[i].nodeType == 1) {
            if (preset.some(el => el == allNodes[i].id)) {
                allNodes[i].childNodes.forEach(el => {
                    if (el.nodeType == 1) {
                        console.log(el);
                        el.style.display = "block";
                    }
                });
            } else {
                allNodes[i].childNodes.forEach(el => {
                    if (el.nodeType == 1) {
                        console.log(el);
                        el.style.display = "none";
                    }
                });
            }
        }
    }
}

function showFiltersVideoCard() {
    const preset = ["prod_section", "price_section", "videoMem_section", "busSize_section", "prodGPU_section", "monitorConSize_section"];
    window.location.href = "#"
    if (document.readyState === "complete") {      
        showFilters(preset);
    } else {
        window.onload = function() {
            showFilters(preset);
        }
    }
}

function showFiltersMother() {
    const preset = ["prod_section", "price_section", "chipset_section", "socket_section", "memoryTypeCpn_section", "memorySlotSize_section", "memoryM2Size_section"];
    window.location.href="#"
    if (document.readyState === "complete") {
        showFilters(preset);
    } else {
        window.onload = function() {
            showFilters(preset);
        };
    }
}

function showCPFilters() {
    const preset = ["prod_section", "price_section", "socket_section", "cpuCores_section", "memoryType_section"];
    window.location.href = "#"
    if (document.readyState === "complete") {
        showFilters(preset);
    } else {
        window.onload = function() {
            showFilters(preset);
        };
    }
}