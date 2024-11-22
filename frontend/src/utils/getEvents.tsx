export const getEvents = async () => {
    const requestOptions = {
        method: "GET",
        redirect: "follow" as RequestRedirect
    };

    try {
        const response = await fetch("http://backend-service:8000/api/v1/events", requestOptions);
        return await response.json();
    } catch (error) {
        console.error(error);
    }
}

export const getEventDetail = async (id) => {
    const requestOptions = {
        method: "GET",
        redirect: "follow" as RequestRedirect
    };

    try {
        const response = await fetch("http://backend-service:8000/api/v1/events/"+id, requestOptions);
        return await response.json();
    } catch (error) {
        console.error(error);
    }
}

