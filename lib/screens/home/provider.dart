import 'package:flutter/widgets.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import 'package:autodo/blocs/todos/barrel.dart';
import 'package:autodo/blocs/tab/barrel.dart';
import 'package:autodo/blocs/stats/barrel.dart';

import 'screen.dart';

/// Structures the BlocProviders for the homescreen and exports them for
/// use by the main screen.
class HomeScreenProvider extends StatelessWidget {
  @override 
  build(BuildContext context) => MultiBlocProvider(
      providers: [
        BlocProvider<TabBloc>(
          create: (context) => TabBloc(),
        ),
        // BlocProvider<FilteredTodosBloc>(
        //   create: (context) => FilteredTodosBloc(
        //     todosBloc: BlocProvider.of<TodosBloc>(context),
        //   ),
        // ),
        BlocProvider<StatsBloc>(
          create: (context) => StatsBloc(
            todosBloc: BlocProvider.of<TodosBloc>(context),
          ),
        ),
      ],
      child: HomeScreen(),
  );
}
