import 'dart:async';

import 'package:equatable/equatable.dart';

import 'package:autodo/models/models.dart';
import 'write_batch_wrapper.dart';

abstract class DataRepository extends Equatable {
  // Todos
  Future<void> addNewTodo(Todo todo);

  Future<void> deleteTodo(Todo todo);

  Stream<List<Todo>> todos();

  Future<void> updateTodo(Todo todo);

  FutureOr<WriteBatchWrapper> startTodoWriteBatch();

  // Refuelings
  Future<void> addNewRefueling(Refueling refueling);

  Future<void> deleteRefueling(Refueling refueling);

  Stream<List<Refueling>> refuelings();

  Future<void> updateRefueling(Refueling refueling);

  FutureOr<WriteBatchWrapper> startRefuelingWriteBatch();

  // Cars
  Future<void> addNewCar(Car car);

  Future<void> deleteCar(Car car);

  Stream<List<Car>> cars();

  Future<void> updateCar(Car car);

  FutureOr<WriteBatchWrapper> startCarWriteBatch();

  // Repeats
  Future<List<Repeat>> addNewRepeat(Repeat repeat);

  Future<void> deleteRepeat(Repeat repeat);

  Stream<List<Repeat>> repeats();

  Future<void> updateRepeat(Repeat repeat);

  FutureOr<WriteBatchWrapper> startRepeatWriteBatch();

  // Notifications
  Stream<int> notificationID();
}
