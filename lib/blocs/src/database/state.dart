import 'package:equatable/equatable.dart';

import 'package:autodo/repositories/repositories.dart';

abstract class DatabaseState extends Equatable {
  const DatabaseState();

  @override
  List<Object> get props => [];
}

class DbUninitialized extends DatabaseState {}

class DbLoaded extends DatabaseState {
  final DataRepository repository;

  const DbLoaded(this.repository);

  @override
  List<Object> get props => [repository];

  @override
  toString() => "DbLoaded { repository: $repository }";
}

class DbNotLoaded extends DatabaseState {}
