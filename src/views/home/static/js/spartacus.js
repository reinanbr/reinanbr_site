const saveMonitoring = () => {
    fetch("https://ipapi.co/json/")
        .then((res) => {
            return res.json()
        }).then((json) => {
            let dt = new Date()
            let infoAccess = {
                site_name:"reinanbr",
                ip: json.ip,
                user_agent: navigator.userAgent,
                site: window.location.href,
                city: json.city,
                state: json.region,
                country: json.country_name,
                provedor: json.org,
                time_unix:dt.valueOf()
            }
            let data = {
                infoAccess:infoAccess
            }
            //console.log(data)
            const requestOptions = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json; charset=utf-8',
                },
                body: JSON.stringify(data),
            };
            fetch(`/api/monitoring/sites`, requestOptions)
                .then((res) => {
                    return res.json()
                })
                .then((json) => {
                    console.log(json)
                }).catch((error) => {
                    console.error(error)
                })

        })
}

saveMonitoring()