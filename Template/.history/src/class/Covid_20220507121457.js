import $ from 'jquery'; 
var

class Covid {
    constructor (hos, active, clinincs, rate, pos, neg, neu){
        this.hos = hos;
        this.active = active;
        this.clinincs = clinincs;
        this.rate = rate;
        this.pos = pos;
        this.neg = neg;
        this.neu = neu;
    }
}

export default Covid