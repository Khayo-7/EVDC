import 'package:flutter/material.dart';
//import 'package:sampleproject2/models/homepage.dart';



class authentication extends StatelessWidget {
  static final String path = "lib/src/pages/login/login1.dart";
  Widget _buildPageContent() {
    return Container(
      padding: EdgeInsets.all(20.0),
      color: Colors.grey.shade800,
      child: ListView(
        children: <Widget>[
          Column(
            children: <Widget>[
              SizedBox(height: 50,),
              Container(width: 200,),
              SizedBox(height: 50,),
              ListTile(
                title: TextField(
                  style: TextStyle(color: Colors.white),
                  decoration: InputDecoration(
                    hintText: "Email address:",
                    hintStyle: TextStyle(color: Colors.white70),
                    border: InputBorder.none,
                    icon: Icon(Icons.email, color: Colors.white30,)
                  ),
                )
              ),
              Divider(color: Colors.grey.shade600,),
              ListTile(
                title: TextField(
                  style: TextStyle(color: Colors.white),
                  decoration: InputDecoration(
                    hintText: "Password:",
                    hintStyle: TextStyle(color: Colors.white70),
                    border: InputBorder.none,
                    icon: Icon(Icons.lock, color: Colors.white30,)
                  ),
                )
              ),
              Divider(color: Colors.grey.shade600,),
              SizedBox(height: 20,),
              Row(
                children: <Widget>[
                  Expanded(
                    child: RaisedButton(
                      onPressed: (){},
                      color: Colors.cyan,
                      child: Text('Login', style: TextStyle(color: Colors.white70, fontSize: 16.0),),
                    ),
                  ),
                ],
              ),
              SizedBox(height: 40,),
              Text('Forgot your password?', style: TextStyle(color: Colors.grey.shade500),)
            ],
          ),
        ],
      ),
    );
  }

  @override
    Widget build(BuildContext context) {
      return Scaffold(
        body: _buildPageContent(),
      );
    }
}

/*class authentication extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: <Widget> [
          Row(mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text('Phone',textAlign: TextAlign.center,style:TextStyle(color: Colors.lightGreen),)
            ,SizedBox(width :10.0),TextField(),
          ],),Column(crossAxisAlignment: CrossAxisAlignment.center,
          children: <Widget>[
            RaisedButton(onPressed: () {
              Navigator.push(context, MaterialPageRoute(builder: (context)=>Homepage()));
            },child: Text('submit',textAlign: TextAlign.center,style: 
            TextStyle(color: Colors.blueAccent))
            )          ],
        

          )
        ]
      )
    );
  }
}*/