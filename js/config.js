var curr_content = null;

function show_view(elem_id) {
    let elem = document.getElementById(elem_id);
    let elem_btn = document.getElementById(elem_id + "_btn");

    if(elem.style.display == "block") {
        hide_view(elem_id);
        return;
    }

    // Hide the old content.
    hide_view(curr_content);
    // Reassign the current content indicator.
    curr_content = elem_id;

    // Switch corresponding interface elems to active.
    elem.style.display = "block";
    elem_btn.classList.add("active_btn");
    elem_btn.classList.remove("inactive_btn");
}

function hide_view(elem_id) {
    let elem = document.getElementById(elem_id);
    let elem_btn = document.getElementById(elem_id + "_btn");

    if(elem == null) {
        return;
    }
    elem.style.display = "none"
    elem_btn.classList.remove("active_btn");
    elem_btn.classList.add("inactive_btn");
}

function toggle_collapsible(elem) {

    // Toggle the active status of the collapsible
    if(elem.classList.contains("active_btn")) {
        show_view(elem.id.slice(0, -4));
    } else {
        hide_view(elem.id.slice(0, -4));
    }
    
    var dropdowns = document.getElementsByClassName("collapsible_content");
    for (i = 0 ; i < dropdowns.length ; i++) {
        if (dropdowns[i].style.display === "flex") {
            dropdowns[i].style.display = "none";
        } else {
            dropdowns[i].style.display = "flex";
        }

        hide_view(dropdowns[i].id.slice(0, -4));
    }
}