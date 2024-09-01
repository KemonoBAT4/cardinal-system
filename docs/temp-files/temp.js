/*########################
# DOPPELMAYR APP SCRIPTS #
########################*/

const apiPrefix = "/api/v1/custom";


/*
    * This script is used to handle the click event on the nav bar items.
    * When a nav bar item is clicked, the user is redirected to the URL specified in the data_href attribute.
*/
document.addEventListener("DOMContentLoaded", function() {
    const navBarItems = document.querySelectorAll(".ob-widget-app-doppelmayr-nav-bar-item-sub-container");

    navBarItems.forEach(item => {
        item.addEventListener("click", function() {
            const href = this.getAttribute("data-href");
            if (href) {
                window.location.href = href;
            }
        });
    });
});


/*
    * This script is used to display the current time in the time span element.
    * The time is updated every second.
*/
document.addEventListener("DOMContentLoaded", function() {
    const timeSpan = document.querySelector(".ob-widget-app-doppelmayr-header-right-data-time-text");

    if (timeSpan) {
        setInterval(() => {
            const date = new Date();
            timeSpan.textContent = date.toLocaleTimeString();
        }, 1000);
    }
});


/*
    * This script is used to create the list items for the selection content container.
    * The list items are created based on the data properties and the API URL specified in the data_properties and data_api_url attributes.
    * When a list item is clicked, the user is redirected to the URL specified in the data_href attribute.
*/
document.addEventListener("DOMContentLoaded", function() {
    const contentContainer = document.querySelector(".ob-widget-app-doppelmayr-selection-content-container");

    if (contentContainer === null) return;

    const subContainer = document.createElement("div");
    subContainer.classList.add("ob-widget-app-doppelmayr-selection-item-sub-container");
    contentContainer.appendChild(subContainer);
    const properties = contentContainer.getAttribute("data-properties").slice(1, -1).split(",").map(property => property.replace(/'/g, "").replace(/\s/g, ""));
    const apiUrl = apiPrefix + contentContainer.getAttribute("data-api_url");
    const baseRedirectUrl = contentContainer.getAttribute("data-base_redirect_url");

    var startDate;

    fetch(apiUrl).then(response => response.json())
        .then(data_list => {
            if (data_list[0]["type"] === "badge") {
                for (let i = 1; i < data_list.length; i++) {
                    const dataObj = data_list[i];
                    /* Creating item contailer */
                    const objContainer = document.createElement("div");
                    objContainer.classList.add("ob-widget-app-doppelmayr-list-item");

                    /* Setting the redirect URL */
                    objContainer.setAttribute("data-href", baseRedirectUrl + dataObj["id"]);

                    /* Creating the property container */
                    const propertyContainer = document.createElement("div");
                    propertyContainer.classList.add("ob-widget-app-doppelmayr-list-item-data");

                    /* Creating the title property container */
                    const titlePropertyContainer = document.createElement("div");
                    const propertyTitle = document.createElement("span");
                    titlePropertyContainer.classList.add("ob-widget-app-doppelmayr-list-item-data");
                    propertyTitle.classList.add("ob-widget-app-doppelmayr-list-item-data-title");
                    propertyTitle.textContent = dataObj["name"] + " " + dataObj["surname"];
                    titlePropertyContainer.appendChild(propertyTitle);
                    propertyContainer.appendChild(titlePropertyContainer);

                    /* Appending the property container to the item container */
                    objContainer.appendChild(propertyContainer);
                    subContainer.appendChild(objContainer);

                    /* Adding the click event listener to the item container */
                    objContainer.addEventListener("click", function() {
                        const href = this.getAttribute("data-href");
                        if (href) {
                            window.location.href = href;
                        }
                    });
                }
            }
            else if (data_list[0]["type"] === "machine") {
                for (let i = 1; i < data_list.length; i++) {
                    const dataObj = data_list[i];
                    /* Creating item contailer */
                    const objContainer = document.createElement("div");
                    objContainer.classList.add("ob-widget-app-doppelmayr-list-item");

                    /* Setting the redirect URL */
                    objContainer.setAttribute("data-href", baseRedirectUrl + dataObj["id"]);

                    /* Creating the property container */
                    const propertyContainer = document.createElement("div");
                    propertyContainer.classList.add("ob-widget-app-doppelmayr-list-item-data");

                    /* Creating the title property container */
                    const titlePropertyContainer = document.createElement("div");
                    const propertyTitle = document.createElement("span");
                    titlePropertyContainer.classList.add("ob-widget-app-doppelmayr-list-item-data");
                    propertyTitle.classList.add("ob-widget-app-doppelmayr-list-item-data-title");
                    propertyTitle.textContent = dataObj["workcenter"] + " | " + dataObj["name"];
                    titlePropertyContainer.appendChild(propertyTitle);
                    propertyContainer.appendChild(titlePropertyContainer);

                    /* Creating the text property container */
                    const textPropertyContainer = document.createElement("div");
                    const propertyText = document.createElement("span");
                    textPropertyContainer.classList.add("ob-widget-app-doppelmayr-list-item-data");
                    propertyText.classList.add("ob-widget-app-doppelmayr-list-item-data-text");
                    propertyText.textContent = dataObj["planned_orders"] + "  |  " + dataObj["working_orders"];
                    textPropertyContainer.appendChild(propertyText);
                    propertyContainer.appendChild(textPropertyContainer);

                    /* Appending the property container to the item container */
                    objContainer.appendChild(propertyContainer);
                    subContainer.appendChild(objContainer);

                    /* Adding the click event listener to the item container */
                    objContainer.addEventListener("click", function() {
                        const href = this.getAttribute("data-href");
                        if (href) {
                            window.location.href = href;
                        }
                    });
                }
            }
            else if (data_list[0]["type"] === "order" && data_list.length > 1) {
                var startDate = data_list[1]["start_date"];

                /* Create the first start date container */
                const startDateContainer = document.createElement("div");
                const startDateText = document.createElement("span");   
                startDateContainer.classList.add("ob-widget-app-doppelmayr-selection-item-start-date-container");
                startDateText.classList.add("ob-widget-app-doppelmayr-selection-item-start-date-text");
                startDateText.textContent = startDate;
                startDateContainer.appendChild(startDateText);
                subContainer.appendChild(startDateContainer);

                // trying to fix the row / grid container
                let grid = document.createElement("div");
                grid.className = "grid";
                subContainer.appendChild(grid);

                /* Iterate through the data list */
                for (let i = 1; i < data_list.length; i++) {
                    /* Check if the start date is different */
                    if(startDate !== data_list[i]["start_date"]) {
                        startDate = data_list[i]["start_date"];
                        console.log("sta modificando la startDate")

                        /* Create the start date container */
                        const startDateContainer = document.createElement("div");
                        const startDateText = document.createElement("span");
                        startDateContainer.classList.add("ob-widget-app-doppelmayr-selection-item-start-date-container");
                        startDateText.classList.add("ob-widget-app-doppelmayr-selection-item-start-date-text");
                        startDateText.textContent = startDate;
                        startDateContainer.appendChild(startDateText);
                        subContainer.appendChild(startDateContainer);
                        
                        grid = document.createElement("div");
                        grid.className = "grid";
                        subContainer.appendChild(grid);
                    }

                    const dataObj = data_list[i];


                    /* Creating item contailer */
                    const objContainer = document.createElement("div");
                    objContainer.classList.add("ob-widget-app-doppelmayr-list-item");
                    
                    /* Setting the redirect URL */
                    objContainer.setAttribute("data-href", baseRedirectUrl + dataObj["id"]);

                    /* Creating the property container */
                    const propertyContainer = document.createElement("div");
                    propertyContainer.classList.add("ob-widget-app-doppelmayr-list-item-data");

                    /* Creating the title property container */
                    // const titlePropertyContainer = document.createElement("div");
                    // const propertyTitle = document.createElement("span");
                    // titlePropertyContainer.classList.add("ob-widget-app-doppelmayr-list-item-data");
                    // propertyTitle.classList.add("ob-widget-app-doppelmayr-list-item-data-title");
                    // propertyTitle.textContent = dataObj["code"];
                    // titlePropertyContainer.appendChild(propertyTitle);
                    // propertyContainer.appendChild(titlePropertyContainer);

                    /* Creating the text property container */
                    const textPropertyContainer = document.createElement("div");
                    const propertyText = document.createElement("span");
                    // TODO: qua il testo del container

                    // textPropertyContainer.classList.add("ob-widget-app-doppelmayr-list-item-data");
                    // propertyText.classList.add("ob-widget-app-doppelmayr-list-item-data-text");
                    // propertyText.textContent = dataObj["article_id"] + " | " + dataObj["description"];
                    // textPropertyContainer.appendChild(propertyText);
                    // propertyContainer.appendChild(textPropertyContainer);

                    /* Give the item container the active id if the status code is working */
                    if (dataObj["status_code"] === "working") {
                        objContainer.id = "working";
                    }

                    //   <|°_°|>

                    /* Appending the property container to the item container */
                    objContainer.appendChild(propertyContainer);
                    // grid.appendChild(objContainer)
                    grid.appendChild(objContainer)
                    // subContainer.appendChild(grid);

                    /* Adding the click event listener to the item container */
                    objContainer.addEventListener("click", function() {
                        const href = this.getAttribute("data-href");
                        if (href) {
                            window.location.href = href;
                        }
                    });
                }
            }
            else {
                for (let i = 1; i < data_list.length; i++) {
                    const dataObj = data_list[i];
                    const objContainer = document.createElement("div");
                    objContainer.classList.add("ob-widget-app-doppelmayr-list-item");
                    for (let j = 0; j < properties.length; j++) {
                        objContainer.setAttribute("data-href", baseRedirectUrl + dataObj["id"]);
                        const property = properties[j];
                        const propertyContainer = document.createElement("div");
                        propertyContainer.classList.add("ob-widget-app-doppelmayr-list-item-data");
                        const propertyText = document.createElement("span");
                        propertyText.classList.add("ob-widget-app-doppelmayr-list-item-data-text");
                        propertyText.textContent = /* property + ": " + */ dataObj[property];
                        propertyContainer.appendChild(propertyText);
                        objContainer.appendChild(propertyContainer);
                    }
                    objContainer.firstElementChild.firstElementChild.className = "ob-widget-app-doppelmayr-list-item-data-title";
                    subContainer.appendChild(objContainer);

                    objContainer.addEventListener("click", function() {
                        const href = this.getAttribute("data-href");
                        if (href) {
                            window.location.href = href;
                        }
                    });
                }
            }
        });
});

function getMachineId() {
    return document.querySelector("#info_container").getAttribute("data-machine_id");
}

function getOrderId() {
    return document.querySelector("#info_container").getAttribute("data-order_id");
}


/*
    * This script is used to display the order information in the info container.
    * The order information is fetched from the API URL specified in the data-api_url attribute.
    * The order information is displayed in the order properties container list.
    * The progress bar is updated based on the progress and total values of the order.
    * The header title is updated based on the machine name.
    * The order code span is updated based on the order name.
    * The order properties container list is updated based on the order properties.
*/
document.addEventListener("DOMContentLoaded", function() {

    const machine_id = getMachineId();
    const order_id = getOrderId();

    if (order_id) {
        const apiUrl = apiPrefix + "/order/" + machine_id + "/" + order_id;

        fetch(apiUrl).then(response => response.json())
            .then(data => {
                const progressBarFg = document.querySelector("#order_progress_bar-fg");
                const orderPropertiesContainerList = document.querySelectorAll("#order_property_value");
                const headerTitle = document.querySelector("#header_title");
                const orderCodeSpan = document.querySelector("#header_order_code")

                headerTitle.textContent = data["machine"]["name"];
                orderCodeSpan.textContent = data["order"]["code"];

                orderPropertiesContainerList.forEach(item => {
                    const property = item.getAttribute("data-property");
                    const value = data["order"][property];
                    item.textContent = value;
                });

                if (progressBarFg) {
                    const root = document.documentElement;

                    const percentage = (data["order"]["progress"] / data["order"]["total"]) * 100;
                    if (percentage < 0) percentage = 0;
                    if (percentage > 100) percentage = 100;

                    root.style.setProperty('--progress-bar-width', `${percentage}%`);
                }
            });
    }
    else if (machine_id) {
        const apiUrl = apiPrefix + "/machine/" + machine_id;

        const headerTitle = document.querySelector("#header_title");

        fetch(apiUrl).then(response => response.json())
            .then(data => {
                headerTitle.textContent = data["name"];
            });
    }
});



/*
    * This script is used to redirect the user to the URL specified in the data_href attribute when the back button is clicked.
*/
document.addEventListener("DOMContentLoaded", function() {
    const listHrefButton = document.querySelectorAll("#herf_button");

    listHrefButton.forEach(item => {
        item.addEventListener("click", function() {
            const href = this.getAttribute("data-href");
            if (href) {
                window.location.href = href;
            }
        });
    });
});


/*
    * This script is used to display the noimage if the image api fails.
*/
document.addEventListener("DOMContentLoaded", function() {
    const imageContainer = document.querySelector("#image_container");

    if(imageContainer) {
        const apiUrl = imageContainer.getAttribute("data-api_url");
        const defaultImage = "/assets/doppelmayr_app/resources/images/noimage.jpg";

        fetch(apiUrl).then(response => {
            if(response.status === 404) {
                console.log("respose status 404.");
                imageContainer.src = defaultImage;
                return;
            }
        });
    }
});

/*
* This script is used to asssign the right values to the table cells.
*/
document.addEventListener("DOMContentLoaded", function() {
    var tableContainer = document.getElementsByClassName("ob-widget-app-doppelmayr-order-dashboard-content-table-container");

    if (tableContainer.length === 0)
        return;

    const machine_id = getMachineId();
    const order_id = getOrderId();

    tableContainer = tableContainer[0];

    const imageButtonContainer = document.querySelector("#image_button").parentElement;
    const imageHref = `/tool/ui/order/view/${machine_id}/${order_id}/image/`;
    imageButtonContainer.setAttribute("data-href", imageHref);
});
