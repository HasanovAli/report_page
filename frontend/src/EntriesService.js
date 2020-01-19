import axios from 'axios';
const API_URL = 'http://localhost:8000';


export default class EntriesService{

    constructor(){}


    getEntriesByUser() {
        const url = `${API_URL}/api/v1/report/entries/`;
        return axios.get(url).then(response => response.data);
    }
    getEntriesByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    // getCustomer(pk) {
    //     const url = `${API_URL}/api/customers/${pk}`;
    //     return axios.get(url).then(response => response.data);
    // }
    deleteEntry(entry){
        const url = `${API_URL}/api/v1/entries/${entry.id}`;
        return axios.delete(url);
    }
    // createCustomer(customer){
    //     const url = `${API_URL}/api/customers/`;
    //     return axios.post(url,customer);
    // }
    // updateCustomer(customer){
    //     const url = `${API_URL}/api/customers/${customer.pk}`;
    //     return axios.put(url,customer);
    // }
}