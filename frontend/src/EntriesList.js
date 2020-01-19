import React, {Component} from 'react';

import EntriesService from './EntriesService';


const entriesService = new EntriesService();

class EntriesList extends Component {

    constructor(props) {
        super(props);

        this.state = {
            entries: [],
            nextPageURL: ''

        };
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete  =  this.handleDelete.bind(this);

    }

    componentDidMount() {
        var self = this;
        entriesService.getEntriesByUser().then(function (result) {
            console.log(result);
            self.setState({entries: result.data, nextPageURL: result.nextlink})
        });
    }

    handleDelete(e,id){
        var  self  =  this;
        entriesService.deleteEntry({id :  id}).then(()=>{
            var  newArr  =  self.state.entries.filter(function(obj) {
                return  obj.id  !==  id;
            });

            self.setState({entries:  newArr})
        });
    }

    nextPage() {
        var self = this;
        console.log(this.state.nextPageURL);
        entriesService.getEntriesByURL(this.state.nextPageURL).then((result) => {

            self.setState({entries: result.data, nextPageURL: result.nextlink})

        });

    }

    render() {
        return (
            <div className="entries--list">
                <table className="table">
                <thead key="thead">
                <tr>
                    <th>#</th>
                    <th>date</th>
                    <th>distance</th>
                    <th>duration</th>
                </tr>
                </thead>

            <tbody>
            {this.state.entries.map( c =>
                    <tr key={c.id}>
                    <td>{c.id}</td>
                    <td>{c.date}</td>
                    <td>{c.distance}</td>
                    <td>{c.duration}</td>
                    <td>
                    <button  onClick={(e)=>  this.handleDelete(e,c.id) }> Delete</button>
        <a href={"/entries/" + c.id}> Update</a>
            </td>
            </tr>
    )}
                </tbody>
        </table>
        <button className="btn btn-primary" onClick={ this.nextPage }>Next</button>

            </div>
    )
        ;
    }
    }

    export default EntriesList;