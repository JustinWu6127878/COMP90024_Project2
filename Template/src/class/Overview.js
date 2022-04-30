class CityOverview {
    constructor (name, state, pop, over, age50, age65, income){
        this.name = name;
        this.state = state;
        this.pop = pop;
        this.over = over;
        this.age50 = age50;
        this.age65 = age65;
        this.income = income;
        this.overper = over/pop;

    }
}

export default CityOverview