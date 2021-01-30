// broker_detail.html
function showAgent(data) {
    generateAgencyHistoryTable(data['history']['agency_history'])
}

function groupByMonth(history) {
    let obj = {}
    for(agency in history) {
        let dates = history[agency]
        for(date of dates) {
            let parts = date.split('-')
            let key = parts[0]+'-'+parts[1]
            if(typeof obj[key] == 'undefined') {
                obj[key] = new Set()
            }
            obj[key].add(agency)
        }
    }
    return obj
}

function generateAgencyHistoryTable(history) {
    const table = document.querySelector('#agency_table')
    const agencies = groupByMonth(history)
    console.log(agencies)
    var keysOrdered = Object.keys(agencies).sort()

    let html = ''
    for(key of keysOrdered) {
        let parts = key.split('-')
        let date = `${getMonth(parts[1])} ${parts[0]}`
        html += `<tr><th scope="row">${date}</th><td>`
        let flag = false
        console.log(agencies[key])
        for(agency of agencies[key]) {
            if(flag) html += ',<br>'
            html += agency
            flag = true
        }
        html += '</td><tr>'
    }
    table.innerHTML = html
}

function find_min_max_year(history) {
    var minimum = new Date().getFullYear()
    var maximum = 0
    for(key in history) {
        historized_object_dates = history[key]
        for(data of historized_object_dates) {
            if(data < minimum) {
                minimum = data
            }
            if(data > maximum) {
                maximum = data
            }
        }
    }
    return {minimum, maximum}
}

showAgent(data)
// \broker_detail.html

function getMonth(month) {
    let monthNames = ['Leden', 'Únor', 'Březen',
                      'Duben', 'Květen', 'Červen',
                      'Červenec', 'Srpen', 'Září',
                      'Říjen', 'Listopad', 'Prosinec']
    let m = parseInt(month)
    return monthNames[m-1]
}