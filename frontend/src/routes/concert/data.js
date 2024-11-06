export const concerts = [{
    slug:"yoona_fan_meeting_tour",
    title: 'YOONA FAN MEETING TOUR : YOONITE in BANGKOK',
    img:"yoona.png",
    dates: [
    { id: 1, date: 'SAT 24 February 2024', time: '18:00' },
    { id: 2, date: 'SUN 25 February 2024', time: '18:00' }
    ],
    venue: 'BITEC Event Hall 98',
    pricing: [
    { tier: 'SO1',coor:"273,230,500,229,500,344,212,343,211,290",shape:"poly", tier_id:1},
    { tier: 'SO2', price: 6500, coor:"211,343,501,450",shape:"rect", tier_id:1 },
    { tier: 'NE1', price: 5500, coor:"528,231,754,230,817,292,815,341,525,342", shape:"poly", tier_id:3 },
    { tier: 'A1', price: 4800, coor:"233,495,499,604",shape:"rect", tier_id:4},
    { tier: 'B1', price: 3800, coor:"233,625,500,627,501,686,434,688,433,707,232,705", shape:"poly", tier_id:5},
    { tier: 'C1', price: 2800, coor:"233,737,433,847", shape:"rect", tier_id:6 },
    { tier: 'S1', price: 2500, coor:"88,353,170,523",shape:"rect", tier_id:7 }
    ],
    seatMap:"/yoona_seat.png",
    seats:[
        { id: 1, No: 1, position: "A1", zone: "SO1", isVacant: true },
        { id: 2, No: 2, position: "A2", zone: "SO1", isVacant: true },
        { id: 3, No: 3, position: "A3", zone: "SO1", isVacant: true },
        { id: 4, No: 4, position: "A4", zone: "SO1", isVacant: true },
        { id: 5, No: 5, position: "A5", zone: "SO1", isVacant: true },
        { id: 6, No: 6, position: "A6", zone: "SO1", isVacant: true },
        { id: 7, No: 7, position: "A7", zone: "SO1", isVacant: true },
        { id: 8, No: 8, position: "A8", zone: "SO1", isVacant: true },
        { id: 9, No: 9, position: "A9", zone: "SO1", isVacant: true },
        { id: 10, No: 10, position: "A10", zone: "SO1", isVacant: true },
        { id: 11, No: 1, position: "B1", zone: "SO1", isVacant: true },
        { id: 12, No: 2, position: "B2", zone: "SO1", isVacant: true },
        { id: 13, No: 3, position: "B3", zone: "SO1", isVacant: true },
        { id: 14, No: 4, position: "B4", zone: "SO1", isVacant: true },
        { id: 15, No: 5, position: "B5", zone: "SO1", isVacant: true },
        { id: 16, No: 6, position: "B6", zone: "SO1", isVacant: true },
        { id: 17, No: 7, position: "B7", zone: "SO1", isVacant: true },
        { id: 18, No: 8, position: "B8", zone: "SO1", isVacant: true },
        { id: 19, No: 9, position: "B9", zone: "SO1", isVacant: true },
        { id: 20, No: 10, position: "B10", zone: "SO1", isVacant: true },
        { id: 21, No: 1, position: "C1", zone: "SO1", isVacant: true },
        { id: 22, No: 2, position: "C2", zone: "SO1", isVacant: true },
        { id: 23, No: 3, position: "C3", zone: "SO1", isVacant: true },
        { id: 24, No: 4, position: "C4", zone: "SO1", isVacant: true },
        { id: 25, No: 5, position: "C5", zone: "SO1", isVacant: true },
        { id: 26, No: 6, position: "C6", zone: "SO1", isVacant: true },
        { id: 27, No: 7, position: "C7", zone: "SO1", isVacant: true },
        { id: 28, No: 8, position: "C8", zone: "SO1", isVacant: true },
        { id: 29, No: 9, position: "C9", zone: "SO1", isVacant: true },
        { id: 30, No: 10, position: "C10", zone: "SO1", isVacant: true },
        { id: 31, No: 1, position: "D1", zone: "SO1", isVacant: true },
        { id: 32, No: 2, position: "D2", zone: "SO1", isVacant: true },
        { id: 33, No: 3, position: "D3", zone: "SO1", isVacant: true },
        { id: 34, No: 4, position: "D4", zone: "SO1", isVacant: true },
        { id: 35, No: 5, position: "D5", zone: "SO1", isVacant: true },
        { id: 36, No: 6, position: "D6", zone: "SO1", isVacant: true },
        { id: 37, No: 7, position: "D7", zone: "SO1", isVacant: true },
        { id: 38, No: 8, position: "D8", zone: "SO1", isVacant: true },
        { id: 39, No: 9, position: "D9", zone: "SO1", isVacant: true },
        { id: 40, No: 10, position: "D10", zone: "SO1", isVacant: true }
    ]
    
    }] 

export const price = [ {
    slug:"yoona_fan_meeting_tour",
    pricing:[
        {tier:1,price:6500, color:"#F7B7D2"},
        {tier:2,price:5500, color:"#EE1067"},
        {tier:3,price:4800, color:"#E8BDB3"},
        {tier:4,price:3800, color:"#F7B7D2"},
        {tier:5,price:2800, color:"#F49194"},
        {tier:6,price:2500, color:"#ED1067"},

    ]
}]