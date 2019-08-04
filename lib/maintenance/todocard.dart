import 'package:flutter/material.dart';
import 'package:autodo/items/items.dart';
import 'package:intl/intl.dart';

class MaintenanceTodoCard extends StatefulWidget {
  final MaintenanceTodoItem item;

  MaintenanceTodoCard({
    @required this.item,
  });

  @override
  State<MaintenanceTodoCard> createState() {
    return MaintenanceTodoCardState();
  }
}

class MaintenanceTodoCardState extends State<MaintenanceTodoCard> {
  bool isChecked = false;

  Transform checkbox(MaintenanceTodoCard widget) {
    return Transform.scale(
      scale: 1.5,
      child: Padding(
        padding: EdgeInsets.fromLTRB(10.0, 0, 10.0, 0),
        child: Checkbox(
          value: isChecked,
          onChanged: (bool val) {
            setState(() {
              isChecked = val;
              widget.item.complete = val;
            });
          },
        ),
      ),
    );
  }

  Row dueDate(DateTime date) {
    bool isDate = date != null;
    if (isDate) {
      return Row(
        children: <Widget>[
          Icon(Icons.alarm, size: 30.0),
          Text('Due on ' + DateFormat("MM/dd/yyyy").format(date)),
        ],
      );
    } else {
      return Row();
    }
  }

  Row dueMileage(int mileage) {
    bool isMileage = mileage != null;
    if (isMileage) {
      return Row(
        children: <Widget>[
          Icon(Icons.directions_car, size: 30.0),
          Text('Due at ' + mileage.toString() + ' miles'),
        ],
      );
    } else {
      return Row();
    }
  }

  Container due(MaintenanceTodoCard widget) {
    return Container(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          dueDate(widget.item.dueDate),
          dueMileage(widget.item.dueMileage),
        ],
      ),
    );
  }

  Column title(MaintenanceTodoCard widget) {
    return Column(
      children: <Widget>[
        Container(
          padding: EdgeInsets.fromLTRB(0.0, 10.0, 0, 0.0),
          alignment: Alignment.center,
          child: Text(
            widget.item.name,
            style: TextStyle(
              fontWeight: FontWeight.w500,
              fontSize: 24.0,
            ),
          ),
        ),
        Divider(),
      ],
    );
  }

  Container body(MaintenanceTodoCard widget) {
    return Container(
      padding: EdgeInsets.fromLTRB(0, 16.0, 0, 16.0),
      child: Row(
        children: <Widget>[
          checkbox(widget),
          due(widget),
        ],
      ),
    );
  }

  Row tags(MaintenanceTodoCard widget) {
    List<Widget> tags = [
      Padding(
        padding: EdgeInsets.only(left: 5.0),
      ),
    ];
    for (var tag in widget.item.tags) {
      tags.add(
        ButtonTheme.fromButtonThemeData(
          data: ButtonThemeData(
            minWidth: 0,
            padding: EdgeInsets.fromLTRB(5.0, 0, 5.0, 0),
          ),
          child: FlatButton(
            child: Chip(
              backgroundColor: Colors.lightGreen,
              label: Text(tag),
            ),
            onPressed: () {},
          ),
        ),
      );
    }
    return Row(
      mainAxisSize: MainAxisSize.max,
      mainAxisAlignment: MainAxisAlignment.start,
      children: tags,
    );
  }

  Row buttons(MaintenanceTodoCard widget) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: <Widget>[
        ButtonTheme.fromButtonThemeData(
          data: ButtonThemeData(
            minWidth: 0,
          ),
          child: FlatButton(
            child: const Icon(Icons.edit),
            onPressed: () {},
          ),
        ),
        ButtonTheme.fromButtonThemeData(
          data: ButtonThemeData(
            minWidth: 0,
          ),
          child: FlatButton(
            child: const Icon(Icons.delete),
            onPressed: () {},
          ),
        ),
      ],
    );
  }

  Row footer(MaintenanceTodoCard widget) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: <Widget>[
        tags(widget),
        buttons(widget),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Container(
        child: Column(
          children: <Widget>[
            title(widget),
            body(widget),
            footer(widget),
          ],
        ),
      ),
    );
  }
}
